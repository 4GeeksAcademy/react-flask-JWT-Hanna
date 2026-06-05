import React from "react";
import { Link, useNavigate } from "react-router-dom";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx"; // <--- El import correcto

export const Navbar = () => {
    const { store, dispatch } = useGlobalReducer(); // <--- Sacamos store y dispatch del hook
    const navigate = useNavigate();

    const handleLogout = () => {
        sessionStorage.removeItem("token");
        dispatch({ type: "clear_token" });
        navigate("/login");
    };

    return (
        <nav className="navbar navbar-light bg-light mb-3 px-3">
            <Link to="/">
                <span className="navbar-brand mb-0 h1">React Flask Auth</span>
            </Link>
            <div className="ml-auto">
                {!store.token ? (
                    <>
                        <Link to="/signup" className="btn btn-outline-primary me-2">
                            Registro
                        </Link>
                        <Link to="/login" className="btn btn-primary">
                            Iniciar Sesión
                        </Link>
                    </>
                ) : (
                    <button className="btn btn-danger" onClick={handleLogout}>
                        Cerrar Sesión
                    </button>
                )}
            </div>
        </nav>
    );
};
