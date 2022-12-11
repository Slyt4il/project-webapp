import React , {useEffect, userEffect, useState} from 'react'

export function ActionBtn(props) {
    const {twitt, action} = props
    const [likes, setLikes] = useState(twitt.likes ? twitt.likes : 0)
    const className = props.className ? props.className : 'btn btn-primary btn-sm'
    const handleClick = (event) => {
        event.preventDefault()
        if (action.type === 'like'){
            setLikes(twitt.likes+1)
        }
    }
    return action.type === 'like' ? <button className={className} onClick={handleClick}> {twitt.likes} Likes</button> : null
  }

export function TwittsComponent(props) {
    const textAreaRef = React.createRef()
    const [newTwitts, setNewTwitts] = useState([])
    const handleSubmit = (event) => {
        event.preventDefault()
        const newVal = textAreaRef.current.value
        let tempNewTwitts = [...newTwitts]
        tempNewTwitts.push({
            content : newVal,
            likes : 0,
            id : 6969
        })
        setNewTwitts(tempNewTwitts)
        textAreaRef.current.value = ''
    }
    return <div className={props.className}>
    <div className='col-12'></div>
        <form onSubmit={handleSubmit}>
        
        <textarea ref={textAreaRef} required={true} className='form-control' placeholder='Say something to the world...!' name='twittit'>

        </textarea>
        <button type='submit' className='btn btn-primary my-3'>Twitt'it</button>
        </form>
        <TwittsList newTwitts={newTwitts}/>
    </div>
}
  
export function Twitt(props) {
    const {twitt} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md'
    return <div className={className}>
      <p>{twitt.id} : {twitt.content}</p>
      <div className='btn btn-group'><ActionBtn twitt={twitt} action={{type:'like'}}></ActionBtn></div>
    </div>
  }

export function TwittsList(props) {
    const [twittsInit, setTwittsInit] = useState([])
    const [twitts, setTwitts] = useState([]) 
    useEffect(()=>{
        const final = [...props.newTwitts].concat(twittsInit)
        if (final.length !== twitts.length)
        {
            setTwitts(final)
        }
        
    }, [props.newTwitts, twitts, twittsInit])
    useEffect(() => {
      const callBack = (response, status) => {
        if (status === 200)
        {
          setTwittsInit(response)
        } else
        {
          alert("An error has occured.")
        }
  }
      loadTwitts(callBack)
  }, [twittsInit])
      return twitts.map((item, index)=>{return <Twitt twitt={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`}  />})
  }

  function loadTwitts(callback) {
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    const url = 'http://localhost:8000/twitts'
    const responseType = 'json'
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = function (e) {
      console.log(e)
      callback({"message" : "Bad request"}, 400)
    }
    xhr.send()
  }