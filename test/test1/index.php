<?php
$urls = array(
'http://www.h-o-g-w-a-r-t-s.com/gryffindor.html',
'http://www.h-o-g-w-a-r-t-s.com/Slytherin.html',
'http://www.h-o-g-w-a-r-t-s.com/Hufflepuff.html',
'http://www.h-o-g-w-a-r-t-s.com/Ravenclaw.html'
);
$url = $urls[array_rand($urls)];
header('Cache-Control: no-cache, no-store, must-revalidate');
header('Pragma: no-cache');
header('Expires: 0');
header('Connection: keep-alive');
header('Expires: '.gmdate('D, d M Y H:i:s \G\M\T', time())); // 1 hour
header('Location: '.$url,true,301);
?>
