import React, { useEffect, useState } from "react";
import { Button } from "@material-ui/core";
import Movie from "../../components/Movie";
import { api } from "../../services/api";
import "./style.css";
import { Search } from "react-feather";
import { TopBar } from "../../components/TopBar";

function Home() {
  const [categories, setCategories] = useState();
  const [movies, setMovies] = useState();
  const [loadingCategories, setLoadingCategories] = useState(true);
  const [loadingMovies, setLoadingMovies] = useState(true);

  useEffect(() => {
    api.get("categories/all").then((response) => {
      setCategories(response.data);
      setLoadingCategories(false);
      console.log(categories)
    });
    api.get(`movies/all`)
    .then((response) => {
      setMovies(response.data);
      console.log(movies)
      setLoadingMovies(false)
    })
  }, []);

  const changeMoviesByCategory = (category) => {
    setLoadingMovies(true)
    api.get(`movies/movie_category/${category}`)
    .then((response) => {
      setMovies(response.data);
      console.log(movies)
      setLoadingMovies(false)
    })  
  }
  return (
    <div className="homeContainer">
      <div className="top-home">
        <TopBar />
      </div>
      <div className="body-home">
        <div className="navBar">
          {!loadingCategories &&
            categories.map((category) => 
              <div onClick={() => changeMoviesByCategory(category.nome_categoria)} className="categoryList" key={category.codigo_categoria}>
                {category.nome_categoria}
              </div>
            )
          }
        </div>
        <div className="movieDisplay">
          <div className="movies">
            {
              !loadingMovies &&
              movies.map((movie) => 
              <Movie className="movieItem" key={movie.codigo_filme} movie={movie}/>
              )
            }
          </div>
        </div>
      </div>
    </div>
  );
}
export default Home;
