import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import coil.compose.rememberImagePainter
import com.example.animateapp.AnimatedMovie
import com.example.animateapp.AnimatedMovieViewModel

@Composable
fun AnimatedMovieInformationScreen(navController: NavController, movie: AnimatedMovie, viewModel: AnimatedMovieViewModel) {
    var isDeleteDialogVisible by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = "Information about ${movie.name}",
            fontSize = 24.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(bottom = 16.dp)
        )

        Text(
            text = "Name: ${movie.name}",
            fontSize = 18.sp,
            modifier = Modifier.padding(bottom = 8.dp)
        )

        Text(
            text = "Studio: ${movie.studio}",
            fontSize = 16.sp,
            modifier = Modifier.padding(bottom = 8.dp)
        )

        Text(
            text = "Description: ${movie.description}",
            fontSize = 16.sp,
            modifier = Modifier.padding(bottom = 8.dp)
        )

        Text(
            text = "Year: ${movie.year}",
            fontSize = 16.sp,
            modifier = Modifier.padding(bottom = 8.dp)
        )

        Text(
            text = "Review: ${movie.review}",
            fontSize = 16.sp,
            modifier = Modifier.padding(bottom = 8.dp)
        )

        Image(
            painter = rememberImagePainter(data = movie.image),
            contentDescription = "Movie Poster",
            modifier = Modifier.fillMaxSize()
        )



        Spacer(modifier = Modifier.weight(1f))

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Button(
                onClick = {
                    navController.navigate("updateMovie/${movie.id}")
                },
                modifier = Modifier.padding(8.dp)
            ) {
                Text("Update")
            }

            Button(
                onClick = {
                    // Show the delete confirmation dialog
                    isDeleteDialogVisible = true
                },
                modifier = Modifier.padding(8.dp)
            ) {
                Text("Delete")
            }

            Button(
                onClick = {
                    navController.popBackStack()
                },
                modifier = Modifier.padding(8.dp)
            ) {
                Text("Go Back")
            }
        }

        if (isDeleteDialogVisible) {
            AlertDialog(
                onDismissRequest = {
                    // Dismiss the dialog if the user cancels
                    isDeleteDialogVisible = false
                },
                title = { Text("Confirm Deletion") },
                text = { Text("Are you sure you want to delete this animated movie?") },
                confirmButton = {
                    Button(
                        onClick = {
                            viewModel.deleteAnimatedMovie(movie.id)
                            navController.popBackStack()
                        }
                    ) {
                        Text("Delete")
                    }
                },
                dismissButton = {
                    Button(
                        onClick = {
                            isDeleteDialogVisible = false
                        }
                    ) {
                        Text("Cancel")
                    }
                }
            )
        }
    }
}
