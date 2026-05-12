import { useEffect, useState } from "react";

import ProductForm from "../components/ProductForm";

import ProductCard from "../components/ProductCard";

import { getProducts } from "../services/productService";


function Home() {

    const [products, setProducts] = useState([]);


    const fetchProducts = async () => {

        try {

            const data = await getProducts();

            setProducts(data);

        } catch (error) {

            console.error(error);
        }
    };


    useEffect(() => {

        fetchProducts();

    }, []);


    return (

        <div className="container py-5">

            <h1 className="text-center mb-5">
                Product Manager
            </h1>


            <div className="row">

                <div className="col-md-4">

                    <ProductForm
                        onProductCreated={fetchProducts}
                    />

                </div>


                <div className="col-md-8">

                    <div className="row g-4">

                        {products.map((product) => (

                            <div
                                className="col-md-6"
                                key={product.id}
                            >

                                <ProductCard
                                    product={product}
                                />

                            </div>

                        ))}

                    </div>

                </div>

            </div>

        </div>
    );
}

export default Home;