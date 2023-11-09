package com.example.animateapp

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddMovieScreen(navController: NavController, viewModel: AnimatedMovieViewModel) {
    var movieName by remember { mutableStateOf("") }
    var movieStudio by remember { mutableStateOf("") }
    var movieDescription by remember { mutableStateOf("") }
    var movieYear by remember { mutableStateOf("") }
    var movieImage by remember { mutableStateOf("") }
    var movieReview by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = "Add an Animated Movie",
            fontSize = 24.sp,
            fontWeight = FontWeight.Bold,
            modifier = Modifier.padding(bottom = 16.dp)
        )

        TextField(
            value = movieName,
            onValueChange = { movieName = it },
            label = { Text("Name") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = movieStudio,
            onValueChange = { movieStudio = it },
            label = { Text("Studio") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = movieDescription,
            onValueChange = { movieDescription = it },
            label = { Text("Description") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = movieYear,
            onValueChange = { movieYear = it },
            label = { Text("Year") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = movieImage,
            onValueChange = { movieImage = it },
            label = { Text("Image URL") },
            modifier = Modifier.padding(8.dp)
        )

        TextField(
            value = movieReview,
            onValueChange = { movieReview = it },
            label = { Text("Review") },
            modifier = Modifier.padding(8.dp)
        )

        Spacer(modifier = Modifier.weight(1f))

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Button(
                onClick = {
                    viewModel.addAnimatedMovie(
                        AnimatedMovie(
                            id = viewModel.getLastAnimatedMovieId() + 1,
                            name = movieName,
                            studio = movieStudio,
                            description = movieDescription,
                            year = movieYear.toIntOrNull() ?: 0,
                            image = movieImage,
                            review = movieReview
                        )
                    )
                    navController.popBackStack()
                },
                modifier = Modifier.padding(8.dp)
            ) {
                Text("Add")
            }

            Button(
                onClick = {
                    navController.popBackStack()
                },
                modifier = Modifier.padding(8.dp)
            ) {
                Text("Cancel")
            }
        }
    }
}
