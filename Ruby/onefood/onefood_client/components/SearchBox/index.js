import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import { FaSearch } from 'react-icons/fa';
import { useRouter } from 'next/router';

export default function SearchBox () {
    const [query, setQuery] = useState ('')
    const router = useRouter()

    async function Search (event){
        event.preventDefault();
        router.push(`/restaurants?q=${query}`)
    }

    return (
        <Form className='d-flex mx-5 my-2' onSubmit={(e) => Search(e)}>
		 <Form.Control
		   type="text"
		   placeholder="Buscar Restaurantes..."
		   value={query}
		   onChange={(e) => setQuery(e.target.value)}
		   className="me-2"
		 />
		 <Button variant="outline-custom-red" type="submit">
		   <FaSearch />
		 </Button>
	   </Form>
    )
}