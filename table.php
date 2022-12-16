<?php
    if($_POST['register'])
    {
        $title=$_POST['title'];
        $fname =$_POST['fname'];
        $lname =$_POST['lname'];
        $email_id=$_POST['email_id'];
        $enterprise_id=$_POST['enterprise_id'];
        $project_name=$_POST['project'];
        $technology=$_POST['technology'];
        $manager=$_POST['manager'];
        $location=$_POST['location']

        $query="INSERT INTO FORM VALUES('$title','$fname','$lname','$email_id','$enterprise_id','$project','$technology','$manager','$location')";
        $data=mysqi_query($conn,$query)
        if ($data)
        {
            echo "Form filled succesfully"
        }
        else{
            echo "Failed please try again"
        }
    }
?>
