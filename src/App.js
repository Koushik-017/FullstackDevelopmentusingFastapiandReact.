import react from 'react'
import {BrowserRouter as Router, Link, Route, Switch} from 'react-router-dom'
import Navbar from"./Components/Navbar"
import { ProductProvider } from './ProductContext'
import ProductTable from './Components/ProductTable'
import AddProducts from'./Components/AddProducts'
import UpdateProduct from'./Components/UpdateProduct'
import { UpdateProductContextProvider } from './UpdateProductContext'


function App() {
  return (
    <div>
      <Router>
        <Switch>
          <ProductProvider>
            <Navbar/>
            <div className="row">
              <div className="col-sm-10 col-xm-12 mr-auto ml-auto mt-4 mb-4">
                <UpdateProductContextProvider>
              
                    <Route exact path='/' component={ProductTable} />
                    <Route exact path='/updateproduct' component={UpdateProduct} />
                  
                    <Route exact path="/addproducts" component={AddProducts} />
             
                </UpdateProductContextProvider>
              
              </div>
            </div>
          </ProductProvider>
        </Switch>
      </Router>
    </div>
  );
}

export default App;