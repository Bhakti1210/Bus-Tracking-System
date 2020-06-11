<?php

	$name1 = $_POST["name1"];
	$mb = $_POST["mb"];

	#create connection 
	$conn = new mysqli('127.0.0.1' , 'root' , '');

	#check connection 
	if($conn->connect_error)
	{
		die("Connection failed: ". $conn->connect_error);
	}

	$sql = "INSERT INTO route( , name) VALUES($mb , '$name1')";

	if(!mysqli_query($conn , $sql))
	{
		echo 'NOT INSERTED';

	}
	else {
			echo 'INSERTED';
		}	
?>