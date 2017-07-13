//
//  CustomCell.swift
//  BinaryCounter
//
//  Created by MJ Norona on 7/12/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class CustomCell: UITableViewCell {
    weak var delegate: ViewController?
    
    var row = 0
    
    @IBAction func subtractButtonPressed(_ sender: UIButton) {
        print(self.tag)
        delegate?.sum -= (delegate?.numbers[self.tag])!
        delegate?.resetSumLabel()
    }
    
    @IBAction func addButtonPressed(_ sender: UIButton) {
        delegate?.sum += (delegate?.numbers[self.tag])!
        delegate?.resetSumLabel()
        
    }
    
    @IBOutlet weak var numberLabel: UILabel!
}
