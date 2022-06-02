import React, { useEffect, useState } from "react";
import { Button } from "@material-ui/core";
import Movie from "../../components/Movie";
import { api } from "../../services/api";
import "./style.css";

function Home() {
  const [categories, setCategories] = useState();
  const [movies, setMovies] = useState();
  useEffect(() => {
    api.get("categories/all").then((response) => {
      setCategories(response.data);
      console.log(categories[0].nome_categoria);
    });
  }, []);

  useEffect(() => {
    api.get("movies/movie_category/Ação").then((response) => {
      setMovies(response.data);
      console.log(movies);
    });
  }, []);
  function handleChangeCategory(category) {
    api.get(`movies/movie_category/${category}`).then((response) => {
      setMovies(response.data);
    });
  }
  return (
    <div className="container">
      <div className="menu">
        <h1 id="title">PurpleTube </h1>
        {categories?.map((element) => (
          <Button
            onClick={() => handleChangeCategory(element.nome_categoria)}
            size="large"
            variant="outlined"
        
            style={{marginTop:"1vw", color:"#FFF" ,width:"15vw"}}
          >
            {element.nome_categoria}
          </Button>
          /*<Category category={String(element.nome_categoria)}/>*/
        ))}
      </div>
      <div className="body">
        <div className="menu-top"></div>

        <div className="movies">
          {movies?.map((element) => (
            <Movie id={element.codigo_filme} duration={element.duracao} />
          ))}
        </div>
      </div>
    </div>
  );
}
export default Home;
