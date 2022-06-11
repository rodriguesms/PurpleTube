import React, { useEffect, useState } from "react";
import { api } from '../../services/api'
import { useNavigate } from 'react-router-dom';
import './style.css'

function LoginPage(){

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [user, setUser] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    var user = localStorage.getItem('user')
    if(user){
      navigate('/')
    }
  }, [])

  const handleSubmit = () => {
    if(email.length > 0 && password.length > 0){
      api
        .post("/users/login", {
          email: email,
          senha: password
        })

        .then((response) => {
          localStorage.setItem('user', JSON.stringify(response.data))
          navigate('/')
        })
        .catch((err) => {
          console.error("ops! aconteceu um erro" + err);
        });
    }

    else
      alert("Email and or password not valid")
    }

  const goToRegister = () => {
    navigate('/register')
  }

  return(
    <div className="page-container">
      <div className="form-box">
        <div className="message">
          <div className="login-title">Login</div>
          <div className="login-subtitle">Entre e aproveite o nosso acervo 100% legalizado.</div>
        </div>
        <form className="login-form">
          <label className="form-item">Email
          <input type={"text"} placeholder="Insira o seu email" value={email} onChange={e => setEmail(e.target.value)} className="input"/>
          </label>
          <label className="form-item">Senha
          <input type={"password"} placeholder="Insira a sua senha" value={password} onChange={e => setPassword(e.target.value)} className="input" />
          </label>
          <div className="buttons">
            <button type="button" onClick={() => handleSubmit()} className="login-button">Entrar</button>
            <label className="register">Novo por aqui?
              <button type="button" onClick={() => goToRegister()} className="register-button">Registrar</button>
            </label>
          </div>
        </form>
        </div>
      </div>
  )
}

export default LoginPage;