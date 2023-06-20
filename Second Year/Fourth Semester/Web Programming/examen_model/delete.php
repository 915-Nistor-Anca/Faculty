<?php 
  session_start();

  if ($_SESSION['logged_in'] == 'false') {
    $_SESSION['login'] = 'Log in';
    $_SESSION['message'] = '';
    header("location: index.php");
  }

  if ($_SESSION['selected_project_id'] == '') {
    header("location: index.php");
  }

  $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $id = $_SESSION['selected_project_id'];
    $sql = "DELETE FROM project WHERE id = '$id'";

    if ($mysqli->query($sql) === true) {
      $_SESSION['selected_project_id'] = '';
      header("location: index.php");
    } else {
      header("location: delete.php");
    }

  }

?>


<!DOCTYPE html>
<html>

<head>
  <title>Projects</title>
  <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>

  <div class="login-page">
    <div class="form">

      <form class="register-form" method="POST" action="delete.php">
        <input class="submit" type="submit" name="delete" value="Click to delete project!">

      </form>

    </div>
  </div>

</body>

</html>