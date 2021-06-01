import useSWR from 'swr';

	export default function getRestaurant(slug) {
	 const fetcher = (...args) => fetch(...args).then((res) => res.json());

	 const { data, error } = useSWR( slug ? `${process.env.apiUrl}/api/restaurants/${slug}` : null,
	   fetcher, { revalidateOnFocus: false }
	)

	 return { restaurant: data, isLoading: !error && !data, isError: error }
	}