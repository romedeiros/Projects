import React from 'react';

import { Navbar, Nav } from 'react-bootstrap';
import Image from 'next/image';
import Link from 'next/link';
import SearchBox from '../SearchBox';
import { useState } from 'react';
import AddressModal from '../AddressModal';
import { FaCrosshairs, FaShoppingBag } from 'react-icons/fa';
import CartModal from '../CartModal';

export default function Header() {
    const [addressModalShow, setAddressModalShow] = useState(false);
    const [cartModalShow, setCartModalShow] = useState(false);

    return(
        <Navbar bg='white' expand='lg' className='border-bottom border-custom-gray'>
            <Navbar.Brand className='mx-3'>
                <Link href='/restaurants'>
                    <a>
                        <Image
                            src='/logo.png'
                            alt='OneFood'
                            width={200}
                            height={44}
                            className='clickable_effect'
                        />
                    </a>
                </Link>
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
		    <Navbar.Collapse id="responsive-navbar-nav" className="justify-content-end">
                <Nav className="me-lg-4 me-sm-0 text-center pt-2 pb-2">
			        <span className="clickable_effect" onClick={() => setCartModalShow(true)}>
			            <FaShoppingBag/> Carrinho
			        </span>
			        <CartModal
			         show={cartModalShow}
			         onHide={() => setCartModalShow(false)}
			         onShow={() => setCartModalShow(true)}
			        />
		        </Nav>
                <Nav className="py-2 text-center">
                <span className="clickable_effect" onClick={() => setAddressModalShow(true)}>
                    <FaCrosshairs className='mb-1'/> Endereço
                </span>
                <AddressModal
                 show={addressModalShow}
                 onHide={() => setAddressModalShow(false)}
                 onShow={() => setAddressModalShow(true)}
                />
		        </Nav>
                <SearchBox />
		    </Navbar.Collapse>
        </Navbar>
    )
}