import { atom } from 'recoil';
import { recoilPersist } from 'recoil-persist';

const { persitAtom } = recoilPersist()

const adrressState = atom ({
    key: 'addressState',
    default: {
        city: '',
        neighborhood: '',
        street: '',
        number: '',
        complement: ''
    },
    effects_UNSTABLE: [persistAtom]
});

export default addressState;
