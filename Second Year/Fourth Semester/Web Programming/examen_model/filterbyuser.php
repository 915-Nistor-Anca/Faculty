<?php
    session_start(); 
    
    $mysqli = new mysqli('localhost', 'root', '', 'examen_model');

    $id = $_SESSION['user_id'];
    $sql = "SELECT * FROM project WHERE projectmanagerid = '$id'";
    $response = mysqli_query($mysqli, $sql);

    if (mysqli_num_rows($response) > 0) {

        while($row = mysqli_fetch_assoc($response)){
            $id = ''. $row['id'] .'';
            $projectmanagerid = ''. $row['projectmanagerid'] .'';
            $name = ''. $row['name'] .'';
            $description = ''. $row['description'] .'';
            $members = ''. $row['members'] .'';
    
            echo '<div style="margin-bottom: 75px; border-top: 1px solid #ddd;">';
            echo '<b><h2 style="margin-left: 20px; margin-right: 20px;">'. $name .'</h2></b>';
            if ($_SESSION['user_id'] == $projectmanagerid) {
                echo '<form method="POST" action="index.php">';
                echo '<button style="margin-bottom: 50px;" class="edit" type="submit" name="update" value="'.$id.'"> Update </button>';
                echo '<button style="margin-bottom: 50px;" class="edit" type="submit" name="delete" value="'.$id.'"> Delete </button>';
                echo '</form>';
              }
            echo '</div>';
        }

    } else {
        echo "No projects.";
    }
    

?>