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

    
    if (isset($_POST['update'])) {
      $_SESSION['selected_document_id'] = $_POST['update'];
      header("location: update.php");
      exit;
    }

  }
?>

<!DOCTYPE html>
<html>

<head>
  <title>Websites and Documents</title>
  <link rel="stylesheet" type="text/css" href="main.css">
  <script src="https://code.jquery.com/jquery-3.3.1.js"></script>
</head>

<body>

  <div style="float: right;">
    <form class="form" style=" height: 46px; padding: 1px;" method="POST" action="index.php">
      <input class="submit" type="submit" name="logout" value="<?= $_SESSION['login']?>">
    </form>
  </div>
    

<center>
    <div id="main">

      <h1> Documents </h1>

        <?php
          
          $sql = "SELECT * FROM documents ORDER BY name DESC";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $idwebsite = ''. $row['idwebsite'] .'';
            $name = ''. $row['name'] .'';
            $keyword1 = ''. $row['keyword1'] .'';
            $keyword2 = ''. $row['keyword2'] .'';
            $keyword3 = ''. $row['keyword3'] .'';
            $keyword4 = ''. $row['keyword4'] .'';
            $keyword5 = ''. $row['keyword5'] .'';

            echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $name .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $id .', '. $idwebsite .'</h4>';
            echo '<h5 style="margin-left: 20px; text-align: left;">'. $keyword1 .', '. $keyword2 .', '. $keyword3 .', '. $keyword4 .', '. $keyword5 .'</h5>';
            //echo $_SESSION['user_id'];
              echo '<form method="POST" action="index.php">';
              echo '<button style="margin-bottom: 50px;" class="edit" type="submit" name="update" value="'.$id.'"> Update </button>';
              echo '</form>';
            
            echo '</div>';
          }

        ?>
      </div>



      <div id="main">

      <h1> Websites </h1>

        <?php
          
          $sql = "SELECT * FROM websites ORDER BY url DESC";
          $response = mysqli_query($mysqli, $sql);

          while($row = mysqli_fetch_array($response)){
            $id = ''. $row['id'] .'';
            $url = ''. $row['url'] .'';

            $sql2 = "SELECT COUNT(*) as count from documents where idwebsite = '$id'";
            $response2 = mysqli_query($mysqli, $sql2);
            $nb = '';
            $nb = mysqli_fetch_assoc($response2)['count'];

            echo '<div style="margin-bottom: 160px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $id .'</h2></b>';
            echo '<h4 style="margin-left: 20px; text-align: left; text-indent: 50px;">'. $url .', '. $nb .'</h4>';
            echo '</div>';
          }

        ?>
      </div>



      <div id="main">
  <h1> Websites </h1>
  <table>
    <tr>
      <th>ID</th>
      <th>URL</th>
      <th>Document Count</th>
    </tr>

    <?php
    $sql = "SELECT * FROM websites ORDER BY url DESC";
    $response = mysqli_query($mysqli, $sql);

    while ($row = mysqli_fetch_array($response)) {
      $id = $row['id'];
      $url = $row['url'];

      $sql2 = "SELECT COUNT(*) AS count FROM documents WHERE idwebsite = '$id'";
      $response2 = mysqli_query($mysqli, $sql2);
      $nb = "";
      $nb = mysqli_fetch_assoc($response2)['count'];

      echo '<tr>';
      echo '<td>' . $id . '</td>';
      echo '<td>' . $url . '</td>';
      echo '<td>' . $nb . '</td>';
      echo '</tr>';
    }
    ?>
    
  </table>
</div>

  </center>
</body>

</html>
      
