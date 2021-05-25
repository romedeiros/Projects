import useSWR from 'swr';
import { useRouter } from 'next/router';

export default function getRestaurants(){
    const fetcher = (...args) => fetch(...args).then((res) => res.json());
    const router = useRouter();

    const { data, error } = useSWR(
        `${process.env.apiUrl}/api/restaurants`,
        fetcher, {revalidateOnFocus: false}
    )

    return{
        restaurants: data,
        isLoading: !error && !data,
        isError: error
    }

}