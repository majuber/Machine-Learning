//
//  ViewController.swift
//  SalaryPrediction
//
//  Created by Juber Moulvi Abdul on 14/11/17.
//  Copyright © 2017 Juber Moulvi Abdul. All rights reserved.
//

import UIKit
import CoreML

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        do {
               let result  = try SalaryPrediction().prediction(Experience: 4)
            print(result.Salary)
        } catch {
            print("error")
        }
        
      
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

