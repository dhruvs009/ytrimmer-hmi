# YouTubeTrimmer Converter
A simple python script to convert YouTube links to YouTubeTrimmer links, using start time, and end time.

## How to start?
1. Clone the repo.<br>
2. Run `pip install -r requirements.txt`<br>
3. Run `python script.py` (or `python3 script.py` if `python` refers to Python2 on your PC).<br>
4. Provide csv filepath, annotator name, converted csv filepath as asked.<br>
5. A file with converted filepath will be created.<br><br>

## Original File Structure
Use the following structure in a csv. The values in the table are just dummy values, the timeframes may not even exist in the video for the examples given.
||||||Add columns here if needed||
|-|-|-|-|-|-|-|
|Operation MBBS|  1|https://www.youtube.com/watch?v=aK-wgYKdBVE|0:11|0:13|...|fear|
|Operation MBBS|  2|https://www.youtube.com/watch?v=i2tZjJ6bxnI|15:27|15:33|...|angry|
|Operation MBBS|  3|https://www.youtube.com/watch?v=lwCU3tuRnuU|123:57|124:05|...|surprised|
|Operation MBBS|  4|https://www.youtube.com/watch?v=mZa-wKePntg|4:01|4:10|...|angry|
|Operation MBBS|  5|https://www.youtube.com/watch?v=hr2CCO0qxDo|10:47|10:56|...|sad|

<br>

## Converted File Structure
Assuming annotator name to be Dhruv, a csv with the following structure is created at the specified path.
|||||||Extra columns appear here||
|-|-|-|-|-|-|-|-|
|Operation MBBS|  2|https://www.youtubetrimmer.com/view/?v=i2tZjJ6bxnI&start=927&end=933|927|933|Dhruv|...|angry|
|Operation MBBS|  4|https://www.youtubetrimmer.com/view/?v=mZa-wKePntg&start=241&end=250|241|250|Dhruv|...|angry|
|Operation MBBS|  1|https://www.youtubetrimmer.com/view/?v=aK-wgYKdBVE&start=11&end=13|11|13|Dhruv|...|fear|
|Operation MBBS|  5|https://www.youtubetrimmer.com/view/?v=hr2CCO0qxDo&start=647&end=656|647|656|Dhruv|...|sad|
|Operation MBBS|  3|https://www.youtubetrimmer.com/view/?v=lwCU3tuRnuU&start=7437&end=7445|7437|7445|Dhruv|...|surprised|
<br>
> [Dhruv Sahnan](https://github.com/dhruvs009)<br>
> IIIT Delhi