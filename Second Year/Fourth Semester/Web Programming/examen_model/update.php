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

  $get_projects = "SELECT * FROM project WHERE id='" . $_SESSION['selected_project_id'] . "'";

  $response = mysqli_query($mysqli, $get_projects);

  while($row = mysqli_fetch_array($response)){
    $projectmanagerid = ''. $row['projectmanagerid'] .'';
    $name = ''. $row['name'] .'';
    $description = ''. $row['description'] .'';
    $members = ''. $row['members'] .'';
  }

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $projectmanagerid = $mysqli->real_escape_string($_POST['projectmanagerid']);
    $name = $mysqli->real_escape_string($_POST['name']);
    $description = $mysqli->real_escape_string($_POST['description']);
    $members = $mysqli->real_escape_string($_POST['members']);

    $id = $_SESSION['selected_project_id'];

    $sql = "UPDATE project SET projectmanagerid = '$projectmanagerid', name = '$name', description = '$description', members = '$members' WHERE id = '$id'";

    if ($mysqli->query($sql) === true) {
      $_SESSION['selected_project_id'] = '';
      header("location: index.php");
    } else {
      header("location: update.php");
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

      <form class="register-form" method="POST" action="update.php">

        <div style="margin-bottom: 15px;">
          <?= $name ?>
        </div>

        <input type="text" placeholder="projectmanagerid" name="projectmanagerid" value="<?= $projectmanagerid ?>" required/>
        <input type="text" placeholder="name" name="name" value="<?= $name ?>" required/>
        <input type="text" placeholder="description" name="description" value="<?= $description ?>" required/>
        <input type="text" placeholder="members" name="members" value="<?= $members ?>" required/>

        <input class="submit" type="submit" name="create" value="Update project">

      </form>

    </div>
  </div>

</body>

</html>