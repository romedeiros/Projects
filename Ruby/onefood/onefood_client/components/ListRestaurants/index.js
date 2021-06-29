import { Col, Row, Spinner, Alert } from 'react-bootstrap';
import Restaurant from './Restaurant';
import getRestaurants from '../../services/getRestaurants';
import Custom404 from '../../pages/404';

export default function ListRestaurantts () {
    const {restaurants, isError, isLoading} = getRestaurants();


    function renderContent(){
        if (isError)
            return <Col><Alert variant='custom-red'>Erro ao carregar</Alert></Col>
        else if (isLoading)
            return <Col><Spinner animation='border' /></Col>
        else if (restaurants.length == 0)
            return <Col><Custom404 /></Col>
        else
            return restaurants.map((restaurant, i) => <Restaurant {...restaurant} key={i}/>)
    }


    return(
        <div className = 'mt-5'>
           <h3 className = 'fw-bold'>Restaurantes</h3>
           <Row>
             {renderContent()}
           </Row>
        </div>
    )
}