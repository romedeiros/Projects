import useSWR from 'swr';
import { useRouter } from 'next/router';
import { useRecoilState } from 'recoil';
import addressState from '../store/atoms/addressAtom';

const fetcher = (...args) => fetch(...args).then((res) => res.json());

export default function getRestaurants(){
    const [address, setAddress] = useRecoilState(addressState);
    const router = useRouter();
    const { category, q } = router.query;

    let params = '';
    if(category)
      params = `${params == '' ? '?' : '&'}category=${category}`
    if(q)
      params = `${params == '' ? '?' : '&'}q=${q}`
    if(address.city != '')
      params = `${params == '' ? '?' : `${params}&`}city=${address.city}`

    const { data, error } = useSWR(
        `${process.env.apiUrl}/api/restaurants${params}`,
        fetcher, {revalidateOnFocus: false}
    )

    return{
        restaurants: data,
        isLoading: !error && !data,
        isError: error
    }

}