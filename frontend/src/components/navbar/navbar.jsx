import React from 'react'
import "./navbar.css"
export default function Navbar({ navbar_items }) {
    return (
        <div className='navbarr'>
            {
                navbar_items.map((item) =>
                    <div className='navbar_item' key={item.path}>
                        <span className='navbar_item_icon'>{item.icon}</span>
                        <span className='navbar_item_name'>{item.name}</span>
                    </div>
                )
            }
        </div>
    )
}
