import { useState, useEffect } from 'react'

const getEcho = async () => {
  const res = await fetch('http://localhost:9090/api/echo/')
  const data = await res.json()
  return data?.msg
}

const getCount = async () => {
  const res = await fetch('http://localhost:9090/api/get-count/')
  const data = await res.json()
  return data?.count
}

const increaseCount = async () => {
  const res = await fetch('http://localhost:9090/api/add-one/', {
    method: 'POST',
  })
  const data = await res.json()
  return data?.count
}

export default function Home() {
  const [echo, setEcho] = useState('')
  const [count, setCount] = useState('')
  const [newCount, setNewCount] = useState('')

  const handleCountRefresh = async () => {
    setCount(await getCount())
  }

  const handleIncreaseCount = async () => {
    const res = await increaseCount()
    setNewCount(res)
  }

  useEffect(async () => {
    setEcho(await getEcho())

    setCount(await getCount())
  }, [])

  return (
    <div className='grid grid-cols-3 my-20 p-4 shadow-2xl'>
      <section className='shadow-lg col-span-1 bg-gray-100 mx-1 p-2'>
        <h1 className='font-bold'>GET: /api/echo/</h1>
        <br />
        <strong>Response:</strong>
        <br />
        <small>{echo}</small>
      </section>

      <section className='shadow-lg col-span-1 bg-gray-100 mx-1 p-2'>
        <h1 className='font-bold'>GET: /api/get-count/</h1>
        <br />
        <strong>Response:</strong>
        <br />
        <small>{count}</small>

        <div className='flex justify-center'>
          <button
            onClick={handleCountRefresh}
            className='bg-gray-300 py-1 px-2 rounded hover:bg-gray-400'
          >
            Refresh
          </button>
        </div>
      </section>

      <section className='shadow-lg col-span-1 bg-gray-100 mx-1 p-2'>
        <h1 className='font-bold'>POST: /api/add-one/</h1>
        <br />
        <strong>Response:</strong>
        <br />
        <small>{newCount}</small>

        <div className='flex justify-center'>
          <button
            onClick={handleIncreaseCount}
            className='bg-gray-300 py-1 px-2 rounded hover:bg-gray-400'
          >
            Increase
          </button>
        </div>
      </section>
    </div>
  )
}
