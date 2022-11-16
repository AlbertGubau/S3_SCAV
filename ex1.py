# This script is able to generate a mosaic video of the 4 different video codecs (VP8, VP9, h265 and AV1)
import os


def mosaic_video(inputfile1, inputfile2, inputfile3, inputfile4):
    # Command line that overlays the 4 videos
    command_line = 'ffmpeg ' \
                   '-i ' + str(inputfile1) + ' -i ' + str(inputfile2) + ' -i ' + str(inputfile3) + ' -i ' + str(
        inputfile4) + ' ' \
                      '-filter_complex "' \
                      'nullsrc=size=1280x720 [base]; ' \
                      '[0:v] setpts=PTS-STARTPTS, scale=640x360 [upperleft];' \
                      '[1:v] setpts=PTS-STARTPTS, scale=640x360 [upperright]; ' \
                      '[2:v] setpts=PTS-STARTPTS, scale=640x360 [lowerleft]; ' \
                      '[3:v] setpts=PTS-STARTPTS, scale=640x360 [lowerright]; ' \
                      '[base][upperleft] overlay=shortest=1 [tmp1]; ' \
                      '[tmp1][upperright] overlay=shortest=1:x=640 [tmp2]; ' \
                      '[tmp2][lowerleft] overlay=shortest=1:y=360 [tmp3]; ' \
                      '[tmp3][lowerright] overlay=shortest=1:x=640:y=360' \
                      '" ' \
                      '-c:v libx264 output_4_videos.mkv'

    # Call the command line from terminal
    os.system(command_line)


# Names of the input videos
input_name1 = "output_480_VP8.webm"
input_name2 = "output_480_VP9.webm"
input_name3 = "output_480_h265.mp4"
input_name4 = "output_480_av1.mkv"

mosaic_video(input_name1, input_name2, input_name3, input_name4)
