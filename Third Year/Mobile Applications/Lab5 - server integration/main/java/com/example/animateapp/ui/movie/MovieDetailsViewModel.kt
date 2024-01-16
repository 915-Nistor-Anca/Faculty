package com.example.animateapp.ui.movie

import android.util.Log
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.animateapp.data.MoviesRepository
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.filterNotNull
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

class MovieDetailsViewModel(
    savedStateHandle: SavedStateHandle,
    private val moviesRepository: MoviesRepository,
) : ViewModel() {

    private val movieId: Int = checkNotNull(savedStateHandle[MovieDetailsDestination.movieIdArg])

    val uiState: StateFlow<MovieDetailsUiState> =
        moviesRepository.getMovieStream(movieId)
            .filterNotNull()
            .map {
                MovieDetailsUiState(outOfStock = it.year <= 0, movieDetails = it.toMovieDetails())
            }.stateIn(
                scope = viewModelScope,
                started = SharingStarted.WhileSubscribed(TIMEOUT_MILLIS),
                initialValue = MovieDetailsUiState()
            )

    fun changeYear() {
        viewModelScope.launch {
            val currentItem = uiState.value.movieDetails.toMovie()
            if (currentItem.year > 0) {
                moviesRepository.updateMovie(currentItem.copy(year = currentItem.year - 1))
            }
        }
    }

    suspend fun deleteMovie() {
        Log.d("DELETEMOVIE", "DELETED MOVIE: ${uiState.value.movieDetails.toMovie()}")
        moviesRepository.deleteMovie(uiState.value.movieDetails.toMovie())
    }

    companion object {
        private const val TIMEOUT_MILLIS = 5_000L
    }
}

data class MovieDetailsUiState(
    val outOfStock: Boolean = true,
    val movieDetails: MovieDetails = MovieDetails()
)