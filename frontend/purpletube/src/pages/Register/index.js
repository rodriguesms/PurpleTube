import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@material-ui/core";
import { api } from "../../services/api";
import './style.css'

function RegisterPage(){

  const [username, setUsername] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const navigate = useNavigate()

  useEffect(() => {
    var user = localStorage.getItem('user')
    if(user){
      navigate('/')
    }
  }, [])

  const handleSubmit = () => {
      if(email.length > 0 && password.length > 0 && username.length > 0){
        api
          .post("/users/", {
            nome_usuario: username,
            email: email,
            senha: password,
            imagem_usuario: ""
          })
          .then((response) => {
            localStorage.setItem('user', JSON.stringify(response.data));
            navigate("/");
          })
          .catch((err) => {
            console.error("ops! aconteceu um erro" + err);
          });
      }
      else
        alert("Email and or password not valid")
  }

  const goToLogin = () => {
    navigate('/login')
  }

  return(
    <div className="page-container">
      <div className="form-box">
        <div className="message">
          <div className="login-title">Registrar</div>
          <div className="login-subtitle">Entre no mais legal acervo legalizado de filmes.</div>
        </div>
        <form className="login-form">
          <label className="form-item">Nome de usuário
            <input type={"text"} placeholder="Insira o seu nome de usuário" value={username} onChange={e => setUsername(e.target.value)} className="input"/>
          </label>
          <label className="form-item">Email
          <input type={"text"} placeholder="Insira o seu email" value={email} onChange={e => setEmail(e.target.value)} className="input"/>
          </label>
          <label className="form-item">Senha
          <input type={"password"} placeholder="Insira a sua senha" value={password} onChange={e => setPassword(e.target.value)} className="input" />
          </label>
          <div className="buttons">
            <button type="button" onClick={() => handleSubmit()} className="register-button">Registrar</button>
            <label className="register">Já é um membro?
              <button type="button" onClick={() => goToLogin()} className="login-button">Entrar</button>
            </label>
          </div>
        </form>
        </div>
      </div>
  )
}

export default RegisterPage;