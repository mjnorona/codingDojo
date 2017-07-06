//
//  ViewController.swift
//  StackViews
//
//  Created by MJ Norona on 7/5/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var player = 1
    var boxValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    @IBOutlet weak var winnerLabel: UILabel!
    
    
    @IBAction func ticButtonPressed(_ sender: UIButton) {
        print(type(of: sender.tag))
        if player == 1 {
            sender.backgroundColor = UIColor.blue
            boxValues[sender.tag-1] = player
            
            print(checkWin())
            if checkWin() {
                
                winnerLabel.text = "Winner is Player \(player)"
                winnerLabel.isHidden = false
            }
            player = 2
        } else {
            sender.backgroundColor = UIColor.red
            boxValues[sender.tag-1] = player
            print(checkWin())
            if checkWin() {
                
                winnerLabel.text = "Winner is Player \(player)"
                winnerLabel.isHidden = false
            }
            player = 1
        }
        print(boxValues)
    }
    
    
    @IBAction func resetButtonPressed(_ sender: UIButton) {
        print("goes here")
        player = 1
        boxValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in 1...10 {
            print(i)
            var tmpButton = self.view.viewWithTag(i) as? UIButton
            tmpButton?.backgroundColor = UIColor.gray
        }
        winnerLabel.isHidden = true
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        winnerLabel.isHidden = true
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
        
    }
    
    func checkWin() -> Bool{
        if boxValues[0] != 0 && boxValues[0] == boxValues[1] && boxValues[0] == boxValues[2]{
            return true
        } else if boxValues[3] != 0 && boxValues[3] == boxValues[4] && boxValues[3] == boxValues[5]{
            return true
        } else if boxValues[6] != 0 && boxValues[6] == boxValues[7] && boxValues[6] == boxValues[8]{
            return true
        } else if boxValues[0] != 0 && boxValues[0] == boxValues[3] && boxValues[0] == boxValues[6]{
            return true
        } else if boxValues[1] != 0 && boxValues[1] == boxValues[4] && boxValues[1] == boxValues[7]{
            return true
        } else if boxValues[2] != 0 && boxValues[2] == boxValues[5] && boxValues[2] == boxValues[8]{
            
            return true
        } else if boxValues[0] != 0 && boxValues[0] == boxValues[4] && boxValues[0] == boxValues[8]{
            return true
        } else if boxValues[6] != 0 && boxValues[6] == boxValues[4] && boxValues[6] == boxValues[2]{
            return true
        } else {
            return false
        }
    }

    
}

