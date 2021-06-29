import Typewriter from '../components/Typewriter';
import { Row, Col } from 'react-bootstrap';
import Image from 'next/image';

export default function Custom404(){
    return (
        <Row>
            <Col md={7} xs={12} className="text-center">
                 <h1 className='fw-bolder text-custom-gray-darker mb-5 lh-base display-5'>
                    <Typewriter text='404 - Página não econtrada' />
                 </h1>
                 <Image 
                        src='/404.jpg'
                        alt='error 404'
                        width={300}
                        height={200}
                  />
            </Col>
        </Row>
    )
}