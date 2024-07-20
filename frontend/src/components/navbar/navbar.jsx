import React, { useState } from 'react'
import "./navbar.css"
export default function Navbar({ navbar_items, selected, onChange }) {
    return (
        <div className='navbarr'>
            <div className='title'>NeuralVisor</div>
            <div className='navbar_items'>
                {
                    navbar_items.map((item) => {
                        const isSelected = item?.name === selected ? true : false;
                        const icon_prefix = item?.icon
                        const icon_suffix = isSelected ? "-dark.svg" : "-light.svg"
                        return (
                            <div onClick={() => onChange(item?.name)} key={item.path} className={isSelected ? "navbar_item_selected" : "navbar_item "} >
                                <span className="navbar_item_icon"><img src={icon_prefix + icon_suffix} alt="icon" /></span>
                                <span className="navbar_item_name">{item?.name}</span>
                            </div>
                        )
                    }
                    )
                }
            </div>
        </div>
    )
}
