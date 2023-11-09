package com.example.animateapp

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
internal fun AnimatedMovieListItem(
    movie: AnimatedMovie,
    onItemClick: (Int) -> Unit,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = Modifier
            .clickable {
                onItemClick(movie.id)

            }
            .fillMaxSize()
            .padding(16.dp),
    ) {
        Text(text = "Name: ${movie.name}", fontSize = 18.sp)
        Text(text = "Studio: ${movie.studio}", fontSize = 16.sp)

    }
}

