package com.example.animateapp.data

import android.content.Context
import android.util.Log
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.io.IOException

interface AppContainer {
    val moviesRepository: MoviesRepository
}

class AppDataContainer(private val context: Context) : AppContainer {

    override val moviesRepository: MoviesRepository by lazy {
        if (true) {
            OnlineMoviesRepository()
        } else {
            OfflineMoviesRepository(AnimateDatabase.getDatabase(context).movieDao())
        }
    }

//    private fun isServerReachable(): Boolean {
//        Log.d("NetworkCheck", "CHECKING IF THE SERVER IS REACHABLE!")
//        return try {
//            val retrofit = Retrofit.Builder()
//                .baseUrl("http://192.168.0.112:5000")
//                .addConverterFactory(GsonConverterFactory.create())
//                .build()
//            Log.d("NetworkCheck", "RETROFIT BUILT!")
//            val moviesApi = retrofit.create(MoviesApi::class.java)
//            Log.d("NetworkCheck", "MOVIES API CREATED!")
//            val response = moviesApi.pingServer()
//            Log.d("NetworkCheck", "RESPONSE RECEIVED: ${response.code()}")
//            val isReachable = response.isSuccessful
//            Log.d("NetworkCheck", "Server is reachable: $isReachable")
//            isReachable
//        } catch (e: IOException) {
//            Log.e("NetworkCheck", "Error checking server reachability", e)
//            false
//        }
//    }

}