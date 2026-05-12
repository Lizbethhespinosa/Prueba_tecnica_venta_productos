import Navbar from "../components/Navbar";

import ProductForm from "../components/ProductForm";


function CreateProduct() {

    return (

        <div className="page-container">

            <Navbar />

            <div className="container py-5 d-flex justify-content-center">

                <div className="newProduct">

                    <ProductForm />

                </div>

            </div>

        </div>
    );
}

export default CreateProduct;