<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=tis-620">
<title>ThaiCreate.Com PHP & MySQL Tutorial</title>
<base href="http://www.oreg.rmutt.ac.th/registrar/">
</head>
<body>
<?php
/**
 * Get a web file (HTML, XHTML, XML, image, etc.) from a URL.  Return an
 * array containing the HTTP server response header fields and content.
 */
function get_web_page( $url, $postvars )
{
$ch      = curl_init( $url );
//    $options = array(
        curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);     // return web page
        curl_setopt($ch,CURLOPT_HEADER,false);    // don't return headers
        curl_setopt($ch,CURLOPT_FOLLOWLOCATION,true);     // follow redirects
        curl_setopt($ch,CURLOPT_ENCODING,"");       // handle all encodings
        curl_setopt($ch,CURLOPT_USERAGENT,"spider"); // who am i
        curl_setopt($ch,CURLOPT_AUTOREFERER,true);     // set referer on redirect
        curl_setopt($ch,CURLOPT_CONNECTTIMEOUT,120);      // timeout on connect
        curl_setopt($ch,CURLOPT_TIMEOUT,120);      // timeout on response
        curl_setopt($ch,CURLOPT_MAXREDIRS,10);       // stop after 10 redirects
	curl_setopt($ch,CURLOPT_POST,1);
	curl_setopt($ch,CURLOPT_POSTFIELDS,$postvars);
//    );

    
    //curl_setopt_array( $ch, $options );
    $content = curl_exec( $ch );
    $err     = curl_errno( $ch );
    $errmsg  = curl_error( $ch );
    $header  = curl_getinfo( $ch );
    curl_close( $ch );

    $header['errno']   = $err;
    $header['errmsg']  = $errmsg;
    $header['content'] = $content;
    return $header;
}
$stdid=$_POST["stdid"]."*";
$url="http://203.158.114.10/registrar/learn_time.asp";
$postvars="f_studentcode=$stdid&f_cmd=1&f_studentnamei=&f_studentsurnamei=&f_studentstatus=all&f_maxrows=1000";
$result=get_web_page($url,$postvars);
$content=$result['content'];
preg_match("'studentid=(.*?)&'si", $content, $match);
if($match[1]) 
	echo "Go to <a target=\"_blank\" onclick=location.href=\"/test1\" href=\"http://203.158.114.10/registrar/impersonate.asp?studentid=$match[1]&cmd=1\">$match[1]</a>";
echo "<br><a href=\"/test1\">Back to Search</a><br>";
preg_match("'<!-- Begin Page Detail -->(.*?)<!-- End Page Detail -->'si", $content, $match);
echo $match[1];
?>
<FORM METHOD=POST ACTION=/test1/search1.php>
studencode: <INPUT TYPE=TEXT NAME=stdid>
<INPUT TYPE=SUBMIT VALUE=Search>
<INPUT TYPE=BUTTON>
</FORM>
<iframe id="fr" src="http://www.youtube.com/subscribe_widget?p=kitarotao" style="overflow: hidden; height: 105px; width: 300px; border: 0;" scrolling="no" frameBorder="0"></iframe>
</body>
</html>
