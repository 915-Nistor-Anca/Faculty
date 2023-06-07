<?php 
  session_start();

  $mysqli = new mysqli('localhost', 'root', '', 'lab7');

  if ($_SESSION['logged_in'] == 'true') {
    header("location: index.php");
  } else {
    $_SESSION['message'] = '';
    $_SESSION['logged_in'] = 'false';
  }

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $username = $_POST['username'];
    $password = md5($_POST['password']);

    $sql = "SELECT * FROM User WHERE username='" . $username . "' AND password='" . $password . "' LIMIT 1";

    $response = mysqli_query($mysqli, $sql);

    if (mysqli_num_rows($response) == 1) {

      while($row = mysqli_fetch_array($response)){
        $_SESSION['user_id'] = ''. $row['id'] .'';
      }

      $_SESSION['message'] = 'Welcome, '. $username .'!';
      $_SESSION['logged_in'] = 'true';
      header("location: index.php");
    }

  }

?>  

<!DOCTYPE html>
<html>

<head>
  <title>News Service</title>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>

  <div class="login-page">
    <div class="form">

      <? echo(md5('password')) ?>

      <form class="login-form" method="POST" action="login.php">

        <input type="text" placeholder="username" name="username" required/>
        <input type="password" placeholder="password" name="password" required/>

        <input class="submit" type="submit" name="login" value="Login">

        <p class="message">Not registered? <a href="register.php">Create an account</a></p>

      </form>

    </div>
  </div>

  <div id="news">

        <?php
          echo 'The current news: </div';
          $sql = "SELECT * FROM News ORDER BY date DESC";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $title = ''. $row['title'] .'';
            $description = ''. $row['content'] .'';
            $producer = ''. $row['producer'] .'';
            $category = ''. $row['category'] .'';
            $date = ''. $row['date'] .'';
            $user_id = ''. $row['user_id'] .'';

            echo '<div style="margin-bottom: 75px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $title .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $description .'</h4>';
            echo '<h5 style="margin-left: 20px; text-align: left;">'. $producer .', '. $category .', '. $date .'</h5>';
            echo '</div>';
          }

        ?>

      </div>

</body>

</html>