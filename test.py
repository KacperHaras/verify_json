import unittest
from main import * 

ex1 = {
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}


ex2 = {
  "PolicyName": "AllAccessPolicy",
  "PolicyDocument": {
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": "*"
      }
    ]
  }
}

ex3 = {
  "PolicyName": "SpecificAccessPolicy",
  "PolicyDocument": {
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "ec2:DescribeInstances",
        "Resource": "arn:aws:ec2:region:account-id:instance/instance-id"
      }
    ]
  }
}

ex4 = {
  "PolicyName": "MixedResourcePolicy",
  "PolicyDocument": {
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "ec2:StartInstances",
          "ec2:StopInstances"
        ],
        "Resource": [
          "arn:aws:ec2:region:account-id:instance/instance-id",
          "*",
          "arn:aws:ec2:region:account-id:volume/volume-id"
        ]
      }
    ]
  }
}

ex5 ={
  "PolicyName": "NestedPolicy",
  "PolicyDocument": {
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "logs:CreateLogStream",
        "Resource": {
          "Fn::Join": [
            ":",
            [
              "arn:aws:logs",
              "region",
              "account-id",
              "log-group",
              "log-stream"
            ]
          ]
        }
      }
    ]
  }
}

ex6 = {
  "PolicyName": "ListResourcePolicy",
  "PolicyDocument": {
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "dynamodb:GetItem",
        "Resource": [
          "arn:aws:dynamodb:region:account-id:table/table-name"
        ]
      }
    ]
  }
}

ex7 = {
  "PolicyName": "EmptyResourcePolicy",
  "PolicyDocument": {
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "sqs:SendMessage",
        "Resource": ""
      }
    ]
  }
}



class TestIAMRolePolicyVerification(unittest.TestCase):
    def test__ex1(self):
        self.assertFalse(json.dumps(ex1['PolicyDocument']))

    def test_ex2(self):
        self.assertFalse(json.dumps(ex2['PolicyDocument']))

    def test_ex3(self):
        self.assertTrue(json.dumps(ex3['PolicyDocument']))

    def test_ex4(self):
        self.assertFalse(json.dumps(ex4['PolicyDocument']))

    def test_ex5(self):
        self.assertTrue(json.dumps(ex5['PolicyDocument']))

    def test_ex6(self):
        self.assertTrue(json.dumps(ex6['PolicyDocument']))

    def test_ex7(self):
        self.assertTrue(json.dumps(ex7['PolicyDocument']))

if __name__ == "__main__":
    unittest.main()
