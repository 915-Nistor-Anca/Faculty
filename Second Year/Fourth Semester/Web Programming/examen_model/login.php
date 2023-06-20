<?php 
  session_start();

  $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

  if ($_SESSION['logged_in'] == 'true') {
    header("location: index.php");
  } else {
    $_SESSION['message'] = '';
    $_SESSION['logged_in'] = 'false';
  }

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $name = $_POST['name'];

    $sql = "SELECT * FROM SoftwareDeveloper WHERE name='" . $name . "'";

    $response = mysqli_query($mysqli, $sql);

    if (mysqli_num_rows($response) == 1) {

      while($row = mysqli_fetch_array($response)){
        $_SESSION['user_id'] = ''. $row['id'] .'';
      }

      $_SESSION['message'] = 'Welcome, '. $name .'!';
      $_SESSION['logged_in'] = 'true';
      header("location: index.php");
    }

  }

?>  

<!DOCTYPE html>
<html>

<head>
  <title>Projects</title>
  <link rel="stylesheet" type="text/css" href="main.css">
  <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
  </head>

<body>

  <div class="login-page">
    <div class="form">

      <form class="login-form" method="POST" action="login.php">

        <input type="text" placeholder="name" name="name" required/>

        <input class="submit" type="submit" name="login" value="Login">

        <p class="message">Are you not registered? <a href="register.php">Create an account</a></p>

      </form>

    </div>
  </div>

</body>

</html>