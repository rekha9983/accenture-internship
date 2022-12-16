<?php include("connection.php");?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
   </head>
<body>
  <div class="container">
    <div class="title">Employement Data</div>
    <div class="content">
      <form action="#">
        <div class="user-details">
            <div class="Title-details">
                <input type="radio" name="Title" id="dot-1">
                <input type="radio" name="Title" id="dot-2">
                <span class="gender-title">Title</span>
                <div class="category">
                  <label for="dot-1">
                  <span class="dot one"></span>
                  <span class="gender">Mr</span>
                </label>
                <label for="dot-2">
                  <span class="dot two"></span>
                  <span class="gender">Ms</span>
                </label>
                
                </div>
              </div>
          <div class="input-box">
            <span class="details">Full Name</span>
            <input type="text" placeholder="Enter your name" required>
          </div>
          <div class="input-box">
            <span class="details">Last name</span>
            <input type="text" placeholder="Enter your Lastname" required>
          </div>
          <div class="input-box">
            <span class="details">Email id</span>
            <input type="text" placeholder="Enter your email id" required>
          </div>
          <div class="input-box">
            <span class="details"> Enterprise id</span>
            <input type="text" placeholder="Enter your Enterprise id" required>
          </div>
          <div class="input-box">
            <span class="details">Project name</span>
            <input type="text" placeholder="Enter your project name" required>
          </div>
          <div class="input-box">
            <span class="details">Techonolgy</span>
            <input type="text" placeholder="Enter your Techonolgy" required>
          </div>
          <div class="input-box">
            <span class="details">Manager</span>
            <input type="text" placeholder="Enter your Manager name" required>
          </div>
          <div class="input-box">
            <span class="details">Location</span>
            <input type="text" placeholder="Enter your Location" required>
          </div>
          <div class="button">
            <input type="submit" value="Employement Data">
        </div>
      </form>
    </div>
  </div>

</body>
</html>