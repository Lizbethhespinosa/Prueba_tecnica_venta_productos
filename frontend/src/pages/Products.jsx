import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";

import ProductCard from "../components/ProductCard";

import { getProducts } from "../services/productService";


function Products() {

    const [products, setProducts] = useState([]);


    const fetchProducts = async () => {

        const data = await getProducts();

        setProducts(data);
    };


    useEffect(() => {

        fetchProducts();

    }, []);


    return (

        <div className="page-container">

            <Navbar />

            <div className="container py-5">

                <div className="row g-4">

                    {products.map((product) => (

                        <div
                            className="col-md-3"
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
    );
}

export default Products;