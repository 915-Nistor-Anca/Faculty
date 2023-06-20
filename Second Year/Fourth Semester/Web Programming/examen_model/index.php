<?php
session_start();
$mysqli = new mysqli('localhost', 'root', '', 'examen_model');

if ($_SESSION['logged_in'] == 'false') 
  {
    $_SESSION['login'] = 'Log in';
    $_SESSION['user_id'] = '';
    header("location: login.php");
  } 
  else 
  {
    $_SESSION['login'] = 'Log out';
  }

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    if (isset($_POST['logout'])) {

      if ($_SESSION['logged_in'] == 'true') {
        $_SESSION['logged_in'] = 'false';
        $_SESSION['message'] = '';
        
        header("location: index.php");
        exit;
      } else {
        header("location: login.php");
        exit;
      }
    }

    if (isset($_POST['add'])) {
      header("location: add.php");
      exit;
    }
    
    if (isset($_POST['update'])) {
      $_SESSION['selected_project_id'] = $_POST['update'];
      header("location: update.php");
      exit;
    }

    if (isset($_POST['delete'])) {
        $_SESSION['selected_project_id'] = $_POST['delete'];
        header("location: delete.php");
        exit;
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

  <div style="float: right;">
    <form class="form" style=" height: 46px; padding: 1px;" method="POST" action="index.php">
      <input class="submit" type="submit" name="logout" value="<?= $_SESSION['login']?>">
    </form>
  </div>

  <div style="float: left;">
    <form class="form" style=" height: 46px; padding: 1px;" method="POST" action="filterbyuser.php">
      <input class="submit" type="submit" name="filter" value="User's projects">
    </form>
  </div>

  <div style="float: right;">
  <form class="form" style=" height: 46px; padding: 1px;" method="POST" action="">
  <input class="submit" type="submit" name="add" value="Add Project">
  </form>
  </div>
    

<center>
    <div id="main">

      <h1> Projects </h1>

      <div id="projects">

        <?php
          
          $sql = "SELECT * FROM Project ORDER BY name DESC";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $projectmanagerid = ''. $row['projectmanagerid'] .'';
            $name = ''. $row['name'] .'';
            $description = ''. $row['description'] .'';
            $members = ''. $row['members'] .'';

            echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $name .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $description .'</h4>';
            echo '<h5 style="margin-left: 20px; text-align: left;">'. $projectmanagerid .', '. $members .'</h5>';
            //echo $_SESSION['user_id'];
            if ($_SESSION['user_id'] == $projectmanagerid) {
              echo '<form method="POST" action="index.php">';
              echo '<button style="margin-bottom: 50px;" class="edit" type="submit" name="update" value="'.$id.'"> Update </button>';
              echo '<button style="margin-bottom: 50px;" class="edit" type="submit" name="delete" value="'.$id.'"> Delete </button>';
              echo '</form>';
            }
            echo '</div>';
          }

        ?>
      </div>
  </center>
</body>

</html>
      
