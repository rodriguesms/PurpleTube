import React, { useEffect, useState } from "react";
import Category from "../../components/Category";
import Movie from "../../components/Movie";
import { api } from "../../services/api";
import "./style.css";

function Home() {
  const [categories, setCategories] = useState();
  useEffect(() => {
    api.get("categories/all").then((response) => {
      setCategories(response.data);
      console.log(categories[0].nome_categoria);
    });
  }, []);
  return (
    <div className="container">
      <div className="menu">
        <h1 id="title">PurpleTube </h1>
        {categories?.map((element) => (
          <Category category={String(element.nome_categoria)} />
        ))}
      </div>
      <div className="body">
        <div className="menu-top">

        </div>
        <div className="movies">
            <Movie/>
            <Movie/>
            <Movie/>
            <Movie/>
            <Movie/>
        </div>
      </div>
    </div>
  );
}
export default Home;
