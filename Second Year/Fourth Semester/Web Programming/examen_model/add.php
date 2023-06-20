<?php 
  session_start();

  if ($_SESSION['logged_in'] == 'false') {
    $_SESSION['login'] = 'Log in';
    $_SESSION['message'] = '';
    header("location: index.php");
  }

  $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $projectmanagerid = $_POST['projectmanagerid'];
    $name = $_POST['name'];
    $description = $_POST['description'];
    $members = $_POST['members'];

    $sql = "INSERT INTO project (projectmanagerid, name, description, members) " . "VALUES ('$projectmanagerid', '$name', '$description', '$members')";

    if ($mysqli->query($sql) === true) {
      header("location: index.php");
    } else {
      $_SESSION['message'] = 'The project could not be saved to the database!';
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

      <form class="register-form" method="POST" action="add.php">

        <div style="margin-bottom: 15px;">
          <?= $_SESSION['message'] ?>
        </div>

        <input type="text" placeholder="projectmanagerid" name="projectmanagerid" value="<?= $_SESSION['user_id'] ?>"required/>
        <input type="text" placeholder="name" name="name" required/>
        <input type="text" placeholder="description" name="description" required/>
        <input type="text" placeholder="members" name="members" required/>

        <input class="submit" type="submit" name="create" value="Create News">

      </form>

    </div>
  </div>

</body>

</html>