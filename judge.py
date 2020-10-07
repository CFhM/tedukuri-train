import os
import argparse
import timeit
import difflib
import sys


def readfile(filename):
    try:
        with open(filename, 'r') as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as e:
        print("Read file Error:", e)
        sys.exit()


def diff_file(filename1, filename2):
    text1_lines = readfile(filename1)
    text2_lines = readfile(filename2)
    if text1_lines != text2_lines:
        d = difflib.HtmlDiff()
        result = d.make_file(text1_lines, text2_lines,
                             filename1, filename2, context=False)
        with open('result.html', 'w') as resultfile:
            resultfile.write(result)
        return False
    return True


def compile(path):
    exec = path[:-4]
    os.system('g++ ' + path + ' -o ' +
              exec + ' -std=c++11 -O2 -DONLINE_JUDGE')


def compare_with_std(sol, std, input, sol_output, std_output):
    start_time = timeit.default_timer()
    os.system('./' + sol + ' <' +
              input + ' >' + sol_output)
    mid_time = timeit.default_timer()
    os.system('./' + std + ' <' +
              input + ' >' + std_output)
    end_time = timeit.default_timer()

    ret = diff_file(sol_output, std_output)
    your_time = mid_time - start_time
    std_time = end_time - mid_time
    return ret, your_time, std_time


def main(args):
    if args.std_file_path != None:
        """
        和标程输入对拍 若输入了数据生成脚本 则采用多轮对拍
        输入建议指定为gen.in 避免破坏test.in
        """
        std_exec_file = args.std_file_path[:-4]
        sol_exec_file = args.file_path[:-4]
        compile(args.file_path)
        compile(args.std_file_path)

        std_output_file_path = 'std.out'
        std_time_total = 0.0
        sol_time_total = 0.0
        if args.gen_script_path != None:
            print('Round = %d' % (args.check_round))
            for i in range(args.check_round):
                os.system('python ' + args.gen_script_path)
                ret, sol_time, std_time = compare_with_std(sol_exec_file, std_exec_file, args.input_file_path,
                                                           args.output_file_path, std_output_file_path)
                if ret == False:
                    print('error at Round %d, difference at \'result.html\'' % (i + 1))
                    exit(-2)

                sol_time_total += sol_time
                std_time_total += std_time

            sol_time_total /= args.check_round
            std_time_total /= args.check_round
            print('AC\nsol average exec time : %f s\nstd average exec time : %f s' % (
                sol_time_total, std_time_total))
        else:
            ret, sol_time, std_time = compare_with_std(sol_exec_file, std_exec_file, args.input_file_path,
                                                       args.output_file_path, std_output_file_path)
            if ret == False:
                print('error at Round %d, difference at \'result.html\'' % (i + 1))
                exit(-2)
            print('AC\nyour exec time : %f s\nstd exec time : %f s' % (
                sol_time, std_time))

    else:
        """
        样例验证
        输入.cpp文件 
        样例输入默认为test.in
        程序输出默认为sol.out
        样例输出默认为test.out
        """
        sol_exec = args.file_path[:-4]
        compile(args.file_path)
        cmd = './' + sol_exec + ' <' + \
            args.input_file_path + ' >' + args.output_file_path
        start_time = timeit.default_timer()
        os.system(cmd)
        end_time = timeit.default_timer()
        print('exec time = %f s\n' % (end_time - start_time))

        sample_output_path = 'test.out'
        ret = diff_file(args.output_file_path, sample_output_path)
        if ret == False:
            print('WA, difference at \'result.html\'')
            exit(-2)
        print('AC')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='file_path',
                        help='input your solution executable file')
    parser.add_argument('-s', '--std', action='store', nargs='?',
                        dest='std_file_path',
                        help='input std executable file for verification')
    parser.add_argument('-i', '--input', action='store', nargs='?', default='test.in',
                        dest='input_file_path',
                        help='input the program\'s input file, redirect the stdin')
    parser.add_argument('-o', '--output', action='store', nargs='?', default='sol.out',
                        dest='output_file_path',
                        help='output file path for necessary.')
    parser.add_argument('-g', '--gen_script', action='store', nargs='?',
                        dest='gen_script_path',
                        help='data generator script path, must be python script, and your generator must output to the input file that you given by -i arg')
    parser.add_argument('-r', '--round', action='store', nargs='?', type=int, default=100,
                        dest='check_round',
                        help='check round for verification, 100 for default, include data generation, run both your code and std code and verify their output.')

    args = parser.parse_args()
    main(args)
