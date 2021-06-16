import Modal from 'react-bootstrap/Modal';
import Cart from '../Cart';
import { useRecoilState } from 'recoil';
import cartState from '../../store/atoms/cartAtom';
import Link from 'next/link';
import Button from 'react-bootstrap/Button';

export default function CartModal(props) {
  const [ cart ] = useRecoilState(cartState);

  return (
    <Modal
      show={props.show}
      size="sm"
      aria-labelledby="contained-modal-title-vcenter"
      centered
      keyboard={false}
      onHide={() => props.onHide()}
    >
      <Modal.Header>
        <h5 className='fw-bold mt-2'>Carrinho</h5>
      </Modal.Header>
      <Modal.Body>
        <Cart show={props.show} />
        {cart.products.length > 0 &&
          <div className="text-center pt-2">
            <Link href='/orders/new'>
              <Button variant="custom-red text-white" onClick={props.onHide}>
                Finalizar pedido
              </Button>            
            </Link>
          </div>
        }
      </Modal.Body>
    </Modal>
  )
}