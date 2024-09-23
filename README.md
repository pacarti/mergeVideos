<h1>mergeVideos</h1>

<p>Uses FFmpeg to merge the video files in MP4, WEBM or MKV format from one directory into one file.</p>

<h2>How it works</h2>

<ul>
  <li>If the folder contains MP4 files only, then output.mp4 file is generated.</li>
  <li>If the folder contains WEBM files only, then output.webm file is generated.</li>
  <li>If the folder contains MKV files only, then output.mkv file is generated.</li>
  <li>If the majority of the files in the folder is in MP4 format, the rest(WEBM or MKV files) will be converted into MP4. Then, output.mp4 file will be generated</li>
  <li>If the majority of the files in the folder is in WEBM format, the rest(MP4 or MKV files) will be converted into WEBM. Then, output.webm file will be generated</li>
  <li>If the majority of the files in the folder is in MKV format, the rest(MP4 or WEBM files) will be converted into MKV. Then, output.mkv file will be generated. <b>Not recommended - in this case, there could be issues with the sound for some files after the merging.</b> What is more advised in this case is to convert all or majority of the files into MP4 or WEBM file formats and then merge it.</li>
</ul>

<p>For all the cases, also the list.txt file is generated. The file contains all the names of the files to be merged. The file is required by FFmpeg.</p>

<p><b>Note: Due to the FFmpeg requirements, the video file names can contain only a-z, A-Z letters, numbers(0-9), dots(.), lowercases(_) and dashes(-). The name CANNOT contain spaces.</b></p>

<h2>Syntax:</h2>
<code>./mergeVideos [path containing the files to be merged]</code>