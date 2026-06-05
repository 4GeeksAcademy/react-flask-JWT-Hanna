import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx"; 

export const Private = () => {
    const { store } = useGlobalReducer(); 
    const navigate = useNavigate();

    useEffect(() => {
        if (!store.token) {
            navigate("/login");
        }
    }, [store.token, navigate]);

    return (
        <div className="container mt-5 text-center">
            <div className="alert alert-danger" role="alert">
                🔒 <strong>Ruta Privada Protegida</strong>
            </div>
            <h1 className="mt-4">¡Bienvenido a tu panel privado!</h1>
            <p className="lead">Si estás viendo esto es porque estás correctamente autenticado.</p>
        </div>
    );
};

