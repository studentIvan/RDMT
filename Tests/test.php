<?php
require '..' . DIRECTORY_SEPARATOR . 'Api' . DIRECTORY_SEPARATOR . 'Rdmt.php';

$control = new Rdmt(3308);

$test = "my simple test";
$test2 = "my simple test2";

for ($i=0; $i<30; $i++) {
	echo ($control->accept($test, 10)) ? "$i. test - accept\n" : "$i. test - not accept\n";
	echo ($control->accept($test2, 20)) ? "$i. test2 - accept\n" : "$i. test2 - not accept\n";
}