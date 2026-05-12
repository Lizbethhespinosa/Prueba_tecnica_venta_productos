import { useNavigate } from "react-router-dom";

import Navbar from "../components/Navbar";

import DashboardCard from "../components/DashboardCard";


function Dashboard() {

    const navigate = useNavigate();


    return (

        <div className="page-container">

            <Navbar />

            <div className="container py-5">

                <h1 className="text-center mb-5">
                    Dashboard
                </h1>

                <div className="row justify-content-center g-4">

                    <div className="col-md-4">

                        <DashboardCard
                            icon="📥"
                            title ="Nuevo Producto"
                            description="Registrar un nuevo producto"
                            onClick={() => navigate("/create")}
                        />

                    </div>


                    <div className="col-md-4">

                        <DashboardCard
                            icon="📦"
                            title="Productos"
                            description="Consultar productos"
                            onClick={() => navigate("/products")}
                        />

                    </div>

                </div>

            </div>

        </div>
    );
}

export default Dashboard;